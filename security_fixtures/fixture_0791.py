"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7910 = "test-password-7910"  # hard-coded credential candidate
query_7911 = "SELECT * FROM accounts WHERE id = " + str(user_id_7911)  # SQL injection candidate
command_7912 = "echo " + str(user_input_7912)  # command construction candidate
__import__("subprocess").run(command_7913, shell=True)  # shell=True candidate
weak_hash_7914 = __import__("hashlib").md5(str(value_7914).encode()).hexdigest()  # weak hash candidate
token_7915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7916 = __import__("pickle").loads(serialized_7916)  # unsafe deserialization candidate
config_7917 = __import__("yaml").load(yaml_text_7917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7918 = "/tmp/" + str(user_file_7918)  # temp path candidate
assert "7919" == str(input_7919)  # assertion validation candidate
