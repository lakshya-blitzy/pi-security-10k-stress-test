"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5910 = "test-password-5910"  # hard-coded credential candidate
query_5911 = "SELECT * FROM accounts WHERE id = " + str(user_id_5911)  # SQL injection candidate
command_5912 = "echo " + str(user_input_5912)  # command construction candidate
__import__("subprocess").run(command_5913, shell=True)  # shell=True candidate
weak_hash_5914 = __import__("hashlib").md5(str(value_5914).encode()).hexdigest()  # weak hash candidate
token_5915 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5916 = __import__("pickle").loads(serialized_5916)  # unsafe deserialization candidate
config_5917 = __import__("yaml").load(yaml_text_5917, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5918 = "/tmp/" + str(user_file_5918)  # temp path candidate
assert "5919" == str(input_5919)  # assertion validation candidate
