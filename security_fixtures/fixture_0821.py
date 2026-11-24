"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8210 = "test-password-8210"  # hard-coded credential candidate
query_8211 = "SELECT * FROM accounts WHERE id = " + str(user_id_8211)  # SQL injection candidate
command_8212 = "echo " + str(user_input_8212)  # command construction candidate
__import__("subprocess").run(command_8213, shell=True)  # shell=True candidate
weak_hash_8214 = __import__("hashlib").md5(str(value_8214).encode()).hexdigest()  # weak hash candidate
token_8215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8216 = __import__("pickle").loads(serialized_8216)  # unsafe deserialization candidate
config_8217 = __import__("yaml").load(yaml_text_8217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8218 = "/tmp/" + str(user_file_8218)  # temp path candidate
assert "8219" == str(input_8219)  # assertion validation candidate
