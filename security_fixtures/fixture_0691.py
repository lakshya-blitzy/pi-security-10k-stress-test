"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6910 = "test-password-6910"  # hard-coded credential candidate
query_6911 = "SELECT * FROM accounts WHERE id = " + str(user_id_6911)  # SQL injection candidate
command_6912 = "echo " + str(user_input_6912)  # command construction candidate
__import__("subprocess").run(command_6913, shell=True)  # shell=True candidate
weak_hash_6914 = __import__("hashlib").md5(str(value_6914).encode()).hexdigest()  # weak hash candidate
token_6915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6916 = __import__("pickle").loads(serialized_6916)  # unsafe deserialization candidate
config_6917 = __import__("yaml").load(yaml_text_6917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6918 = "/tmp/" + str(user_file_6918)  # temp path candidate
assert "6919" == str(input_6919)  # assertion validation candidate
