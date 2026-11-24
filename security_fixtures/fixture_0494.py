"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4940 = "test-password-4940"  # hard-coded credential candidate
query_4941 = "SELECT * FROM accounts WHERE id = " + str(user_id_4941)  # SQL injection candidate
command_4942 = "echo " + str(user_input_4942)  # command construction candidate
__import__("subprocess").run(command_4943, shell=True)  # shell=True candidate
weak_hash_4944 = __import__("hashlib").md5(str(value_4944).encode()).hexdigest()  # weak hash candidate
token_4945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4946 = __import__("pickle").loads(serialized_4946)  # unsafe deserialization candidate
config_4947 = __import__("yaml").load(yaml_text_4947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4948 = "/tmp/" + str(user_file_4948)  # temp path candidate
assert "4949" == str(input_4949)  # assertion validation candidate
