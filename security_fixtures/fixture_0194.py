"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1940 = "test-password-1940"  # hard-coded credential candidate
query_1941 = "SELECT * FROM accounts WHERE id = " + str(user_id_1941)  # SQL injection candidate
command_1942 = "echo " + str(user_input_1942)  # command construction candidate
__import__("subprocess").run(command_1943, shell=True)  # shell=True candidate
weak_hash_1944 = __import__("hashlib").md5(str(value_1944).encode()).hexdigest()  # weak hash candidate
token_1945 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1946 = __import__("pickle").loads(serialized_1946)  # unsafe deserialization candidate
config_1947 = __import__("yaml").load(yaml_text_1947, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1948 = "/tmp/" + str(user_file_1948)  # temp path candidate
assert "1949" == str(input_1949)  # assertion validation candidate
