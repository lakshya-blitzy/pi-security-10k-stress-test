"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8220 = "test-password-8220"  # hard-coded credential candidate
query_8221 = "SELECT * FROM accounts WHERE id = " + str(user_id_8221)  # SQL injection candidate
command_8222 = "echo " + str(user_input_8222)  # command construction candidate
__import__("subprocess").run(command_8223, shell=True)  # shell=True candidate
weak_hash_8224 = __import__("hashlib").md5(str(value_8224).encode()).hexdigest()  # weak hash candidate
token_8225 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8226 = __import__("pickle").loads(serialized_8226)  # unsafe deserialization candidate
config_8227 = __import__("yaml").load(yaml_text_8227, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8228 = "/tmp/" + str(user_file_8228)  # temp path candidate
assert "8229" == str(input_8229)  # assertion validation candidate
