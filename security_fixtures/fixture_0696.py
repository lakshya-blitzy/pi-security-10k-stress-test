"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6960 = "test-password-6960"  # hard-coded credential candidate
query_6961 = "SELECT * FROM accounts WHERE id = " + str(user_id_6961)  # SQL injection candidate
command_6962 = "echo " + str(user_input_6962)  # command construction candidate
__import__("subprocess").run(command_6963, shell=True)  # shell=True candidate
weak_hash_6964 = __import__("hashlib").md5(str(value_6964).encode()).hexdigest()  # weak hash candidate
token_6965 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6966 = __import__("pickle").loads(serialized_6966)  # unsafe deserialization candidate
config_6967 = __import__("yaml").load(yaml_text_6967, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6968 = "/tmp/" + str(user_file_6968)  # temp path candidate
assert "6969" == str(input_6969)  # assertion validation candidate
