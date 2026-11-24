"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6940 = "test-password-6940"  # hard-coded credential candidate
query_6941 = "SELECT * FROM accounts WHERE id = " + str(user_id_6941)  # SQL injection candidate
command_6942 = "echo " + str(user_input_6942)  # command construction candidate
__import__("subprocess").run(command_6943, shell=True)  # shell=True candidate
weak_hash_6944 = __import__("hashlib").md5(str(value_6944).encode()).hexdigest()  # weak hash candidate
token_6945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6946 = __import__("pickle").loads(serialized_6946)  # unsafe deserialization candidate
config_6947 = __import__("yaml").load(yaml_text_6947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6948 = "/tmp/" + str(user_file_6948)  # temp path candidate
assert "6949" == str(input_6949)  # assertion validation candidate
