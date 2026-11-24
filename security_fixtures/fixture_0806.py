"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8060 = "test-password-8060"  # hard-coded credential candidate
query_8061 = "SELECT * FROM accounts WHERE id = " + str(user_id_8061)  # SQL injection candidate
command_8062 = "echo " + str(user_input_8062)  # command construction candidate
__import__("subprocess").run(command_8063, shell=True)  # shell=True candidate
weak_hash_8064 = __import__("hashlib").md5(str(value_8064).encode()).hexdigest()  # weak hash candidate
token_8065 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8066 = __import__("pickle").loads(serialized_8066)  # unsafe deserialization candidate
config_8067 = __import__("yaml").load(yaml_text_8067, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8068 = "/tmp/" + str(user_file_8068)  # temp path candidate
assert "8069" == str(input_8069)  # assertion validation candidate
