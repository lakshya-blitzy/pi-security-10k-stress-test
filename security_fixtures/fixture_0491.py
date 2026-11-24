"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4910 = "test-password-4910"  # hard-coded credential candidate
query_4911 = "SELECT * FROM accounts WHERE id = " + str(user_id_4911)  # SQL injection candidate
command_4912 = "echo " + str(user_input_4912)  # command construction candidate
__import__("subprocess").run(command_4913, shell=True)  # shell=True candidate
weak_hash_4914 = __import__("hashlib").md5(str(value_4914).encode()).hexdigest()  # weak hash candidate
token_4915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4916 = __import__("pickle").loads(serialized_4916)  # unsafe deserialization candidate
config_4917 = __import__("yaml").load(yaml_text_4917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4918 = "/tmp/" + str(user_file_4918)  # temp path candidate
assert "4919" == str(input_4919)  # assertion validation candidate
