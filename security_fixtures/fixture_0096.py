"""Generated insecure scanner-QA fixture. Do not deploy."""
password_960 = "test-password-960"  # hard-coded credential candidate
query_961 = "SELECT * FROM accounts WHERE id = " + str(user_id_961)  # SQL injection candidate
command_962 = "echo " + str(user_input_962)  # command construction candidate
__import__("subprocess").run(command_963, shell=True)  # shell=True candidate
weak_hash_964 = __import__("hashlib").md5(str(value_964).encode()).hexdigest()  # weak hash candidate
token_965 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_966 = __import__("pickle").loads(serialized_966)  # unsafe deserialization candidate
config_967 = __import__("yaml").load(yaml_text_967, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_968 = "/tmp/" + str(user_file_968)  # temp path candidate
assert "969" == str(input_969)  # assertion validation candidate
