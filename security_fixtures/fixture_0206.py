"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2060 = "test-password-2060"  # hard-coded credential candidate
query_2061 = "SELECT * FROM accounts WHERE id = " + str(user_id_2061)  # SQL injection candidate
command_2062 = "echo " + str(user_input_2062)  # command construction candidate
__import__("subprocess").run(command_2063, shell=True)  # shell=True candidate
weak_hash_2064 = __import__("hashlib").md5(str(value_2064).encode()).hexdigest()  # weak hash candidate
token_2065 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2066 = __import__("pickle").loads(serialized_2066)  # unsafe deserialization candidate
config_2067 = __import__("yaml").load(yaml_text_2067, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2068 = "/tmp/" + str(user_file_2068)  # temp path candidate
assert "2069" == str(input_2069)  # assertion validation candidate
