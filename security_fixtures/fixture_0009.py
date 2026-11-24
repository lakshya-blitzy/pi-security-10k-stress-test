"""Generated insecure scanner-QA fixture. Do not deploy."""
password_90 = "test-password-90"  # hard-coded credential candidate
query_91 = "SELECT * FROM accounts WHERE id = " + str(user_id_91)  # SQL injection candidate
command_92 = "echo " + str(user_input_92)  # command construction candidate
__import__("subprocess").run(command_93, shell=True)  # shell=True candidate
weak_hash_94 = __import__("hashlib").md5(str(value_94).encode()).hexdigest()  # weak hash candidate
token_95 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_96 = __import__("pickle").loads(serialized_96)  # unsafe deserialization candidate
config_97 = __import__("yaml").load(yaml_text_97, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_98 = "/tmp/" + str(user_file_98)  # temp path candidate
assert "99" == str(input_99)  # assertion validation candidate
