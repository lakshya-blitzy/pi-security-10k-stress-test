"""Generated insecure scanner-QA fixture. Do not deploy."""
password_80 = "test-password-80"  # hard-coded credential candidate
query_81 = "SELECT * FROM accounts WHERE id = " + str(user_id_81)  # SQL injection candidate
command_82 = "echo " + str(user_input_82)  # command construction candidate
__import__("subprocess").run(command_83, shell=True)  # shell=True candidate
weak_hash_84 = __import__("hashlib").md5(str(value_84).encode()).hexdigest()  # weak hash candidate
token_85 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_86 = __import__("pickle").loads(serialized_86)  # unsafe deserialization candidate
config_87 = __import__("yaml").load(yaml_text_87, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_88 = "/tmp/" + str(user_file_88)  # temp path candidate
assert "89" == str(input_89)  # assertion validation candidate
