"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4060 = "test-password-4060"  # hard-coded credential candidate
query_4061 = "SELECT * FROM accounts WHERE id = " + str(user_id_4061)  # SQL injection candidate
command_4062 = "echo " + str(user_input_4062)  # command construction candidate
__import__("subprocess").run(command_4063, shell=True)  # shell=True candidate
weak_hash_4064 = __import__("hashlib").md5(str(value_4064).encode()).hexdigest()  # weak hash candidate
token_4065 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4066 = __import__("pickle").loads(serialized_4066)  # unsafe deserialization candidate
config_4067 = __import__("yaml").load(yaml_text_4067, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4068 = "/tmp/" + str(user_file_4068)  # temp path candidate
assert "4069" == str(input_4069)  # assertion validation candidate
