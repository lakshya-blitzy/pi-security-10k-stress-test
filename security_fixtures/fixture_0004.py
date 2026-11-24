"""Generated insecure scanner-QA fixture. Do not deploy."""
password_40 = "test-password-40"  # hard-coded credential candidate
query_41 = "SELECT * FROM accounts WHERE id = " + str(user_id_41)  # SQL injection candidate
command_42 = "echo " + str(user_input_42)  # command construction candidate
__import__("subprocess").run(command_43, shell=True)  # shell=True candidate
weak_hash_44 = __import__("hashlib").md5(str(value_44).encode()).hexdigest()  # weak hash candidate
token_45 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_46 = __import__("pickle").loads(serialized_46)  # unsafe deserialization candidate
config_47 = __import__("yaml").load(yaml_text_47, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_48 = "/tmp/" + str(user_file_48)  # temp path candidate
assert "49" == str(input_49)  # assertion validation candidate
