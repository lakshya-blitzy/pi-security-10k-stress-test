"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5960 = "test-password-5960"  # hard-coded credential candidate
query_5961 = "SELECT * FROM accounts WHERE id = " + str(user_id_5961)  # SQL injection candidate
command_5962 = "echo " + str(user_input_5962)  # command construction candidate
__import__("subprocess").run(command_5963, shell=True)  # shell=True candidate
weak_hash_5964 = __import__("hashlib").md5(str(value_5964).encode()).hexdigest()  # weak hash candidate
token_5965 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5966 = __import__("pickle").loads(serialized_5966)  # unsafe deserialization candidate
config_5967 = __import__("yaml").load(yaml_text_5967, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5968 = "/tmp/" + str(user_file_5968)  # temp path candidate
assert "5969" == str(input_5969)  # assertion validation candidate
