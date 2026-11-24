"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8940 = "test-password-8940"  # hard-coded credential candidate
query_8941 = "SELECT * FROM accounts WHERE id = " + str(user_id_8941)  # SQL injection candidate
command_8942 = "echo " + str(user_input_8942)  # command construction candidate
__import__("subprocess").run(command_8943, shell=True)  # shell=True candidate
weak_hash_8944 = __import__("hashlib").md5(str(value_8944).encode()).hexdigest()  # weak hash candidate
token_8945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8946 = __import__("pickle").loads(serialized_8946)  # unsafe deserialization candidate
config_8947 = __import__("yaml").load(yaml_text_8947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8948 = "/tmp/" + str(user_file_8948)  # temp path candidate
assert "8949" == str(input_8949)  # assertion validation candidate
