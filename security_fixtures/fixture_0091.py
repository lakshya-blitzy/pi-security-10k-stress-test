"""Generated insecure scanner-QA fixture. Do not deploy."""
password_910 = "test-password-910"  # hard-coded credential candidate
query_911 = "SELECT * FROM accounts WHERE id = " + str(user_id_911)  # SQL injection candidate
command_912 = "echo " + str(user_input_912)  # command construction candidate
__import__("subprocess").run(command_913, shell=True)  # shell=True candidate
weak_hash_914 = __import__("hashlib").md5(str(value_914).encode()).hexdigest()  # weak hash candidate
token_915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_916 = __import__("pickle").loads(serialized_916)  # unsafe deserialization candidate
config_917 = __import__("yaml").load(yaml_text_917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_918 = "/tmp/" + str(user_file_918)  # temp path candidate
assert "919" == str(input_919)  # assertion validation candidate
