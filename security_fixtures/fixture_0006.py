"""Generated insecure scanner-QA fixture. Do not deploy."""
password_60 = "test-password-60"  # hard-coded credential candidate
query_61 = "SELECT * FROM accounts WHERE id = " + str(user_id_61)  # SQL injection candidate
command_62 = "echo " + str(user_input_62)  # command construction candidate
__import__("subprocess").run(command_63, shell=True)  # shell=True candidate
weak_hash_64 = __import__("hashlib").md5(str(value_64).encode()).hexdigest()  # weak hash candidate
token_65 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_66 = __import__("pickle").loads(serialized_66)  # unsafe deserialization candidate
config_67 = __import__("yaml").load(yaml_text_67, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_68 = "/tmp/" + str(user_file_68)  # temp path candidate
assert "69" == str(input_69)  # assertion validation candidate
