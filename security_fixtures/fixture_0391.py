"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3910 = "test-password-3910"  # hard-coded credential candidate
query_3911 = "SELECT * FROM accounts WHERE id = " + str(user_id_3911)  # SQL injection candidate
command_3912 = "echo " + str(user_input_3912)  # command construction candidate
__import__("subprocess").run(command_3913, shell=True)  # shell=True candidate
weak_hash_3914 = __import__("hashlib").md5(str(value_3914).encode()).hexdigest()  # weak hash candidate
token_3915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3916 = __import__("pickle").loads(serialized_3916)  # unsafe deserialization candidate
config_3917 = __import__("yaml").load(yaml_text_3917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3918 = "/tmp/" + str(user_file_3918)  # temp path candidate
assert "3919" == str(input_3919)  # assertion validation candidate
